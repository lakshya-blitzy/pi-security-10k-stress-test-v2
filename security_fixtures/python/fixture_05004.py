"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50040 = "qa_fixture_token_50040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50041 = "SELECT * FROM users WHERE id = " + str(user_input_50041)  # SQL injection candidate
OS_COMMAND_50042 = "convert " + user_path_50042  # command construction candidate
EXEC_RESULT_50043 = __import__("subprocess").run(OS_COMMAND_50043, shell=True)  # shell execution candidate
WEAK_HASH_50044 = __import__("hashlib").md5(payload_50044.encode()).hexdigest()  # weak hash
NONCE_50045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50046 = __import__("pickle").loads(serialized_50046)  # unsafe deserialization
YAML_OBJECT_50047 = __import__("yaml").load(yaml_text_50047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50048 = "/srv/data/" + request_path_50048  # path traversal candidate
assert supplied_50049 == expected_50049  # input validation candidate
