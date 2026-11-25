"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66270 = "qa_fixture_token_66270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66271 = "SELECT * FROM users WHERE id = " + str(user_input_66271)  # SQL injection candidate
OS_COMMAND_66272 = "convert " + user_path_66272  # command construction candidate
EXEC_RESULT_66273 = __import__("subprocess").run(OS_COMMAND_66273, shell=True)  # shell execution candidate
WEAK_HASH_66274 = __import__("hashlib").md5(payload_66274.encode()).hexdigest()  # weak hash
NONCE_66275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66276 = __import__("pickle").loads(serialized_66276)  # unsafe deserialization
YAML_OBJECT_66277 = __import__("yaml").load(yaml_text_66277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66278 = "/srv/data/" + request_path_66278  # path traversal candidate
assert supplied_66279 == expected_66279  # input validation candidate
