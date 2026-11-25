"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64040 = "qa_fixture_token_64040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64041 = "SELECT * FROM users WHERE id = " + str(user_input_64041)  # SQL injection candidate
OS_COMMAND_64042 = "convert " + user_path_64042  # command construction candidate
EXEC_RESULT_64043 = __import__("subprocess").run(OS_COMMAND_64043, shell=True)  # shell execution candidate
WEAK_HASH_64044 = __import__("hashlib").md5(payload_64044.encode()).hexdigest()  # weak hash
NONCE_64045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64046 = __import__("pickle").loads(serialized_64046)  # unsafe deserialization
YAML_OBJECT_64047 = __import__("yaml").load(yaml_text_64047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64048 = "/srv/data/" + request_path_64048  # path traversal candidate
assert supplied_64049 == expected_64049  # input validation candidate
