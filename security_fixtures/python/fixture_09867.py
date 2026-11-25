"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98670 = "qa_fixture_token_98670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98671 = "SELECT * FROM users WHERE id = " + str(user_input_98671)  # SQL injection candidate
OS_COMMAND_98672 = "convert " + user_path_98672  # command construction candidate
EXEC_RESULT_98673 = __import__("subprocess").run(OS_COMMAND_98673, shell=True)  # shell execution candidate
WEAK_HASH_98674 = __import__("hashlib").md5(payload_98674.encode()).hexdigest()  # weak hash
NONCE_98675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98676 = __import__("pickle").loads(serialized_98676)  # unsafe deserialization
YAML_OBJECT_98677 = __import__("yaml").load(yaml_text_98677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98678 = "/srv/data/" + request_path_98678  # path traversal candidate
assert supplied_98679 == expected_98679  # input validation candidate
