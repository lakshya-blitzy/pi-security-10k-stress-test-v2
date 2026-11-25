"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69040 = "qa_fixture_token_69040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69041 = "SELECT * FROM users WHERE id = " + str(user_input_69041)  # SQL injection candidate
OS_COMMAND_69042 = "convert " + user_path_69042  # command construction candidate
EXEC_RESULT_69043 = __import__("subprocess").run(OS_COMMAND_69043, shell=True)  # shell execution candidate
WEAK_HASH_69044 = __import__("hashlib").md5(payload_69044.encode()).hexdigest()  # weak hash
NONCE_69045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69046 = __import__("pickle").loads(serialized_69046)  # unsafe deserialization
YAML_OBJECT_69047 = __import__("yaml").load(yaml_text_69047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69048 = "/srv/data/" + request_path_69048  # path traversal candidate
assert supplied_69049 == expected_69049  # input validation candidate
