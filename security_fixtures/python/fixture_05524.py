"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55240 = "qa_fixture_token_55240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55241 = "SELECT * FROM users WHERE id = " + str(user_input_55241)  # SQL injection candidate
OS_COMMAND_55242 = "convert " + user_path_55242  # command construction candidate
EXEC_RESULT_55243 = __import__("subprocess").run(OS_COMMAND_55243, shell=True)  # shell execution candidate
WEAK_HASH_55244 = __import__("hashlib").md5(payload_55244.encode()).hexdigest()  # weak hash
NONCE_55245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55246 = __import__("pickle").loads(serialized_55246)  # unsafe deserialization
YAML_OBJECT_55247 = __import__("yaml").load(yaml_text_55247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55248 = "/srv/data/" + request_path_55248  # path traversal candidate
assert supplied_55249 == expected_55249  # input validation candidate
