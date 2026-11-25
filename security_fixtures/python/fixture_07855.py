"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78550 = "qa_fixture_token_78550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78551 = "SELECT * FROM users WHERE id = " + str(user_input_78551)  # SQL injection candidate
OS_COMMAND_78552 = "convert " + user_path_78552  # command construction candidate
EXEC_RESULT_78553 = __import__("subprocess").run(OS_COMMAND_78553, shell=True)  # shell execution candidate
WEAK_HASH_78554 = __import__("hashlib").md5(payload_78554.encode()).hexdigest()  # weak hash
NONCE_78555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78556 = __import__("pickle").loads(serialized_78556)  # unsafe deserialization
YAML_OBJECT_78557 = __import__("yaml").load(yaml_text_78557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78558 = "/srv/data/" + request_path_78558  # path traversal candidate
assert supplied_78559 == expected_78559  # input validation candidate
