"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51500 = "qa_fixture_token_51500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51501 = "SELECT * FROM users WHERE id = " + str(user_input_51501)  # SQL injection candidate
OS_COMMAND_51502 = "convert " + user_path_51502  # command construction candidate
EXEC_RESULT_51503 = __import__("subprocess").run(OS_COMMAND_51503, shell=True)  # shell execution candidate
WEAK_HASH_51504 = __import__("hashlib").md5(payload_51504.encode()).hexdigest()  # weak hash
NONCE_51505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51506 = __import__("pickle").loads(serialized_51506)  # unsafe deserialization
YAML_OBJECT_51507 = __import__("yaml").load(yaml_text_51507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51508 = "/srv/data/" + request_path_51508  # path traversal candidate
assert supplied_51509 == expected_51509  # input validation candidate
