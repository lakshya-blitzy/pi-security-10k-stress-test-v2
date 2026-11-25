"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56870 = "qa_fixture_token_56870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56871 = "SELECT * FROM users WHERE id = " + str(user_input_56871)  # SQL injection candidate
OS_COMMAND_56872 = "convert " + user_path_56872  # command construction candidate
EXEC_RESULT_56873 = __import__("subprocess").run(OS_COMMAND_56873, shell=True)  # shell execution candidate
WEAK_HASH_56874 = __import__("hashlib").md5(payload_56874.encode()).hexdigest()  # weak hash
NONCE_56875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56876 = __import__("pickle").loads(serialized_56876)  # unsafe deserialization
YAML_OBJECT_56877 = __import__("yaml").load(yaml_text_56877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56878 = "/srv/data/" + request_path_56878  # path traversal candidate
assert supplied_56879 == expected_56879  # input validation candidate
