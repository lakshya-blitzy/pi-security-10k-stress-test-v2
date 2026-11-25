"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52040 = "qa_fixture_token_52040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52041 = "SELECT * FROM users WHERE id = " + str(user_input_52041)  # SQL injection candidate
OS_COMMAND_52042 = "convert " + user_path_52042  # command construction candidate
EXEC_RESULT_52043 = __import__("subprocess").run(OS_COMMAND_52043, shell=True)  # shell execution candidate
WEAK_HASH_52044 = __import__("hashlib").md5(payload_52044.encode()).hexdigest()  # weak hash
NONCE_52045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52046 = __import__("pickle").loads(serialized_52046)  # unsafe deserialization
YAML_OBJECT_52047 = __import__("yaml").load(yaml_text_52047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52048 = "/srv/data/" + request_path_52048  # path traversal candidate
assert supplied_52049 == expected_52049  # input validation candidate
