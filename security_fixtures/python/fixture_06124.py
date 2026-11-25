"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61240 = "qa_fixture_token_61240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61241 = "SELECT * FROM users WHERE id = " + str(user_input_61241)  # SQL injection candidate
OS_COMMAND_61242 = "convert " + user_path_61242  # command construction candidate
EXEC_RESULT_61243 = __import__("subprocess").run(OS_COMMAND_61243, shell=True)  # shell execution candidate
WEAK_HASH_61244 = __import__("hashlib").md5(payload_61244.encode()).hexdigest()  # weak hash
NONCE_61245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61246 = __import__("pickle").loads(serialized_61246)  # unsafe deserialization
YAML_OBJECT_61247 = __import__("yaml").load(yaml_text_61247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61248 = "/srv/data/" + request_path_61248  # path traversal candidate
assert supplied_61249 == expected_61249  # input validation candidate
