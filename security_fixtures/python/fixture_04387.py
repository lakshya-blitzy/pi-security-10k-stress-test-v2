"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43870 = "qa_fixture_token_43870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43871 = "SELECT * FROM users WHERE id = " + str(user_input_43871)  # SQL injection candidate
OS_COMMAND_43872 = "convert " + user_path_43872  # command construction candidate
EXEC_RESULT_43873 = __import__("subprocess").run(OS_COMMAND_43873, shell=True)  # shell execution candidate
WEAK_HASH_43874 = __import__("hashlib").md5(payload_43874.encode()).hexdigest()  # weak hash
NONCE_43875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43876 = __import__("pickle").loads(serialized_43876)  # unsafe deserialization
YAML_OBJECT_43877 = __import__("yaml").load(yaml_text_43877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43878 = "/srv/data/" + request_path_43878  # path traversal candidate
assert supplied_43879 == expected_43879  # input validation candidate
