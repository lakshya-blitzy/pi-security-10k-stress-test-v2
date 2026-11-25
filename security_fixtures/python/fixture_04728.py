"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47280 = "qa_fixture_token_47280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47281 = "SELECT * FROM users WHERE id = " + str(user_input_47281)  # SQL injection candidate
OS_COMMAND_47282 = "convert " + user_path_47282  # command construction candidate
EXEC_RESULT_47283 = __import__("subprocess").run(OS_COMMAND_47283, shell=True)  # shell execution candidate
WEAK_HASH_47284 = __import__("hashlib").md5(payload_47284.encode()).hexdigest()  # weak hash
NONCE_47285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47286 = __import__("pickle").loads(serialized_47286)  # unsafe deserialization
YAML_OBJECT_47287 = __import__("yaml").load(yaml_text_47287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47288 = "/srv/data/" + request_path_47288  # path traversal candidate
assert supplied_47289 == expected_47289  # input validation candidate
