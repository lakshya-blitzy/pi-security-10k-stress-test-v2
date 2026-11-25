"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56240 = "qa_fixture_token_56240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56241 = "SELECT * FROM users WHERE id = " + str(user_input_56241)  # SQL injection candidate
OS_COMMAND_56242 = "convert " + user_path_56242  # command construction candidate
EXEC_RESULT_56243 = __import__("subprocess").run(OS_COMMAND_56243, shell=True)  # shell execution candidate
WEAK_HASH_56244 = __import__("hashlib").md5(payload_56244.encode()).hexdigest()  # weak hash
NONCE_56245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56246 = __import__("pickle").loads(serialized_56246)  # unsafe deserialization
YAML_OBJECT_56247 = __import__("yaml").load(yaml_text_56247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56248 = "/srv/data/" + request_path_56248  # path traversal candidate
assert supplied_56249 == expected_56249  # input validation candidate
