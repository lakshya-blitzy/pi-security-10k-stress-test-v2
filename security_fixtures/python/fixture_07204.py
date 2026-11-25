"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72040 = "qa_fixture_token_72040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72041 = "SELECT * FROM users WHERE id = " + str(user_input_72041)  # SQL injection candidate
OS_COMMAND_72042 = "convert " + user_path_72042  # command construction candidate
EXEC_RESULT_72043 = __import__("subprocess").run(OS_COMMAND_72043, shell=True)  # shell execution candidate
WEAK_HASH_72044 = __import__("hashlib").md5(payload_72044.encode()).hexdigest()  # weak hash
NONCE_72045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72046 = __import__("pickle").loads(serialized_72046)  # unsafe deserialization
YAML_OBJECT_72047 = __import__("yaml").load(yaml_text_72047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72048 = "/srv/data/" + request_path_72048  # path traversal candidate
assert supplied_72049 == expected_72049  # input validation candidate
