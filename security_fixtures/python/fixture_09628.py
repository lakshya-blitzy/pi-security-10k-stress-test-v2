"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96280 = "qa_fixture_token_96280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96281 = "SELECT * FROM users WHERE id = " + str(user_input_96281)  # SQL injection candidate
OS_COMMAND_96282 = "convert " + user_path_96282  # command construction candidate
EXEC_RESULT_96283 = __import__("subprocess").run(OS_COMMAND_96283, shell=True)  # shell execution candidate
WEAK_HASH_96284 = __import__("hashlib").md5(payload_96284.encode()).hexdigest()  # weak hash
NONCE_96285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96286 = __import__("pickle").loads(serialized_96286)  # unsafe deserialization
YAML_OBJECT_96287 = __import__("yaml").load(yaml_text_96287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96288 = "/srv/data/" + request_path_96288  # path traversal candidate
assert supplied_96289 == expected_96289  # input validation candidate
