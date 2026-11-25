"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51040 = "qa_fixture_token_51040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51041 = "SELECT * FROM users WHERE id = " + str(user_input_51041)  # SQL injection candidate
OS_COMMAND_51042 = "convert " + user_path_51042  # command construction candidate
EXEC_RESULT_51043 = __import__("subprocess").run(OS_COMMAND_51043, shell=True)  # shell execution candidate
WEAK_HASH_51044 = __import__("hashlib").md5(payload_51044.encode()).hexdigest()  # weak hash
NONCE_51045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51046 = __import__("pickle").loads(serialized_51046)  # unsafe deserialization
YAML_OBJECT_51047 = __import__("yaml").load(yaml_text_51047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51048 = "/srv/data/" + request_path_51048  # path traversal candidate
assert supplied_51049 == expected_51049  # input validation candidate
