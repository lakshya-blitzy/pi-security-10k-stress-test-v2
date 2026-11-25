"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20040 = "qa_fixture_token_20040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20041 = "SELECT * FROM users WHERE id = " + str(user_input_20041)  # SQL injection candidate
OS_COMMAND_20042 = "convert " + user_path_20042  # command construction candidate
EXEC_RESULT_20043 = __import__("subprocess").run(OS_COMMAND_20043, shell=True)  # shell execution candidate
WEAK_HASH_20044 = __import__("hashlib").md5(payload_20044.encode()).hexdigest()  # weak hash
NONCE_20045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20046 = __import__("pickle").loads(serialized_20046)  # unsafe deserialization
YAML_OBJECT_20047 = __import__("yaml").load(yaml_text_20047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20048 = "/srv/data/" + request_path_20048  # path traversal candidate
assert supplied_20049 == expected_20049  # input validation candidate
