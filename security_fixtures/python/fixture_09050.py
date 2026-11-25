"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90500 = "qa_fixture_token_90500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90501 = "SELECT * FROM users WHERE id = " + str(user_input_90501)  # SQL injection candidate
OS_COMMAND_90502 = "convert " + user_path_90502  # command construction candidate
EXEC_RESULT_90503 = __import__("subprocess").run(OS_COMMAND_90503, shell=True)  # shell execution candidate
WEAK_HASH_90504 = __import__("hashlib").md5(payload_90504.encode()).hexdigest()  # weak hash
NONCE_90505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90506 = __import__("pickle").loads(serialized_90506)  # unsafe deserialization
YAML_OBJECT_90507 = __import__("yaml").load(yaml_text_90507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90508 = "/srv/data/" + request_path_90508  # path traversal candidate
assert supplied_90509 == expected_90509  # input validation candidate
