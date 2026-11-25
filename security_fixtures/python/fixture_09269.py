"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92690 = "qa_fixture_token_92690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92691 = "SELECT * FROM users WHERE id = " + str(user_input_92691)  # SQL injection candidate
OS_COMMAND_92692 = "convert " + user_path_92692  # command construction candidate
EXEC_RESULT_92693 = __import__("subprocess").run(OS_COMMAND_92693, shell=True)  # shell execution candidate
WEAK_HASH_92694 = __import__("hashlib").md5(payload_92694.encode()).hexdigest()  # weak hash
NONCE_92695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92696 = __import__("pickle").loads(serialized_92696)  # unsafe deserialization
YAML_OBJECT_92697 = __import__("yaml").load(yaml_text_92697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92698 = "/srv/data/" + request_path_92698  # path traversal candidate
assert supplied_92699 == expected_92699  # input validation candidate
