"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97040 = "qa_fixture_token_97040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97041 = "SELECT * FROM users WHERE id = " + str(user_input_97041)  # SQL injection candidate
OS_COMMAND_97042 = "convert " + user_path_97042  # command construction candidate
EXEC_RESULT_97043 = __import__("subprocess").run(OS_COMMAND_97043, shell=True)  # shell execution candidate
WEAK_HASH_97044 = __import__("hashlib").md5(payload_97044.encode()).hexdigest()  # weak hash
NONCE_97045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97046 = __import__("pickle").loads(serialized_97046)  # unsafe deserialization
YAML_OBJECT_97047 = __import__("yaml").load(yaml_text_97047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97048 = "/srv/data/" + request_path_97048  # path traversal candidate
assert supplied_97049 == expected_97049  # input validation candidate
