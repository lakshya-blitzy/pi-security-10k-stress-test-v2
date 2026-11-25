"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55500 = "qa_fixture_token_55500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55501 = "SELECT * FROM users WHERE id = " + str(user_input_55501)  # SQL injection candidate
OS_COMMAND_55502 = "convert " + user_path_55502  # command construction candidate
EXEC_RESULT_55503 = __import__("subprocess").run(OS_COMMAND_55503, shell=True)  # shell execution candidate
WEAK_HASH_55504 = __import__("hashlib").md5(payload_55504.encode()).hexdigest()  # weak hash
NONCE_55505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55506 = __import__("pickle").loads(serialized_55506)  # unsafe deserialization
YAML_OBJECT_55507 = __import__("yaml").load(yaml_text_55507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55508 = "/srv/data/" + request_path_55508  # path traversal candidate
assert supplied_55509 == expected_55509  # input validation candidate
