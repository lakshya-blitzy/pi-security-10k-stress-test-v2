"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79040 = "qa_fixture_token_79040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79041 = "SELECT * FROM users WHERE id = " + str(user_input_79041)  # SQL injection candidate
OS_COMMAND_79042 = "convert " + user_path_79042  # command construction candidate
EXEC_RESULT_79043 = __import__("subprocess").run(OS_COMMAND_79043, shell=True)  # shell execution candidate
WEAK_HASH_79044 = __import__("hashlib").md5(payload_79044.encode()).hexdigest()  # weak hash
NONCE_79045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79046 = __import__("pickle").loads(serialized_79046)  # unsafe deserialization
YAML_OBJECT_79047 = __import__("yaml").load(yaml_text_79047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79048 = "/srv/data/" + request_path_79048  # path traversal candidate
assert supplied_79049 == expected_79049  # input validation candidate
