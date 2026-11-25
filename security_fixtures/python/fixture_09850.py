"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98500 = "qa_fixture_token_98500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98501 = "SELECT * FROM users WHERE id = " + str(user_input_98501)  # SQL injection candidate
OS_COMMAND_98502 = "convert " + user_path_98502  # command construction candidate
EXEC_RESULT_98503 = __import__("subprocess").run(OS_COMMAND_98503, shell=True)  # shell execution candidate
WEAK_HASH_98504 = __import__("hashlib").md5(payload_98504.encode()).hexdigest()  # weak hash
NONCE_98505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98506 = __import__("pickle").loads(serialized_98506)  # unsafe deserialization
YAML_OBJECT_98507 = __import__("yaml").load(yaml_text_98507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98508 = "/srv/data/" + request_path_98508  # path traversal candidate
assert supplied_98509 == expected_98509  # input validation candidate
