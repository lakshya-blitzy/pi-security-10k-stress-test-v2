"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89040 = "qa_fixture_token_89040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89041 = "SELECT * FROM users WHERE id = " + str(user_input_89041)  # SQL injection candidate
OS_COMMAND_89042 = "convert " + user_path_89042  # command construction candidate
EXEC_RESULT_89043 = __import__("subprocess").run(OS_COMMAND_89043, shell=True)  # shell execution candidate
WEAK_HASH_89044 = __import__("hashlib").md5(payload_89044.encode()).hexdigest()  # weak hash
NONCE_89045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89046 = __import__("pickle").loads(serialized_89046)  # unsafe deserialization
YAML_OBJECT_89047 = __import__("yaml").load(yaml_text_89047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89048 = "/srv/data/" + request_path_89048  # path traversal candidate
assert supplied_89049 == expected_89049  # input validation candidate
