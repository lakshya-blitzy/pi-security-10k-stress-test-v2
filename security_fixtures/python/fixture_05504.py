"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55040 = "qa_fixture_token_55040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55041 = "SELECT * FROM users WHERE id = " + str(user_input_55041)  # SQL injection candidate
OS_COMMAND_55042 = "convert " + user_path_55042  # command construction candidate
EXEC_RESULT_55043 = __import__("subprocess").run(OS_COMMAND_55043, shell=True)  # shell execution candidate
WEAK_HASH_55044 = __import__("hashlib").md5(payload_55044.encode()).hexdigest()  # weak hash
NONCE_55045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55046 = __import__("pickle").loads(serialized_55046)  # unsafe deserialization
YAML_OBJECT_55047 = __import__("yaml").load(yaml_text_55047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55048 = "/srv/data/" + request_path_55048  # path traversal candidate
assert supplied_55049 == expected_55049  # input validation candidate
