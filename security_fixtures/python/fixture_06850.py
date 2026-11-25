"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68500 = "qa_fixture_token_68500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68501 = "SELECT * FROM users WHERE id = " + str(user_input_68501)  # SQL injection candidate
OS_COMMAND_68502 = "convert " + user_path_68502  # command construction candidate
EXEC_RESULT_68503 = __import__("subprocess").run(OS_COMMAND_68503, shell=True)  # shell execution candidate
WEAK_HASH_68504 = __import__("hashlib").md5(payload_68504.encode()).hexdigest()  # weak hash
NONCE_68505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68506 = __import__("pickle").loads(serialized_68506)  # unsafe deserialization
YAML_OBJECT_68507 = __import__("yaml").load(yaml_text_68507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68508 = "/srv/data/" + request_path_68508  # path traversal candidate
assert supplied_68509 == expected_68509  # input validation candidate
