"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4040 = "qa_fixture_token_4040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4041 = "SELECT * FROM users WHERE id = " + str(user_input_4041)  # SQL injection candidate
OS_COMMAND_4042 = "convert " + user_path_4042  # command construction candidate
EXEC_RESULT_4043 = __import__("subprocess").run(OS_COMMAND_4043, shell=True)  # shell execution candidate
WEAK_HASH_4044 = __import__("hashlib").md5(payload_4044.encode()).hexdigest()  # weak hash
NONCE_4045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4046 = __import__("pickle").loads(serialized_4046)  # unsafe deserialization
YAML_OBJECT_4047 = __import__("yaml").load(yaml_text_4047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4048 = "/srv/data/" + request_path_4048  # path traversal candidate
assert supplied_4049 == expected_4049  # input validation candidate
