"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78870 = "qa_fixture_token_78870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78871 = "SELECT * FROM users WHERE id = " + str(user_input_78871)  # SQL injection candidate
OS_COMMAND_78872 = "convert " + user_path_78872  # command construction candidate
EXEC_RESULT_78873 = __import__("subprocess").run(OS_COMMAND_78873, shell=True)  # shell execution candidate
WEAK_HASH_78874 = __import__("hashlib").md5(payload_78874.encode()).hexdigest()  # weak hash
NONCE_78875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78876 = __import__("pickle").loads(serialized_78876)  # unsafe deserialization
YAML_OBJECT_78877 = __import__("yaml").load(yaml_text_78877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78878 = "/srv/data/" + request_path_78878  # path traversal candidate
assert supplied_78879 == expected_78879  # input validation candidate
