"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83040 = "qa_fixture_token_83040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83041 = "SELECT * FROM users WHERE id = " + str(user_input_83041)  # SQL injection candidate
OS_COMMAND_83042 = "convert " + user_path_83042  # command construction candidate
EXEC_RESULT_83043 = __import__("subprocess").run(OS_COMMAND_83043, shell=True)  # shell execution candidate
WEAK_HASH_83044 = __import__("hashlib").md5(payload_83044.encode()).hexdigest()  # weak hash
NONCE_83045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83046 = __import__("pickle").loads(serialized_83046)  # unsafe deserialization
YAML_OBJECT_83047 = __import__("yaml").load(yaml_text_83047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83048 = "/srv/data/" + request_path_83048  # path traversal candidate
assert supplied_83049 == expected_83049  # input validation candidate
