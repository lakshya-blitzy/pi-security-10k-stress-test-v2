"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29870 = "qa_fixture_token_29870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29871 = "SELECT * FROM users WHERE id = " + str(user_input_29871)  # SQL injection candidate
OS_COMMAND_29872 = "convert " + user_path_29872  # command construction candidate
EXEC_RESULT_29873 = __import__("subprocess").run(OS_COMMAND_29873, shell=True)  # shell execution candidate
WEAK_HASH_29874 = __import__("hashlib").md5(payload_29874.encode()).hexdigest()  # weak hash
NONCE_29875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29876 = __import__("pickle").loads(serialized_29876)  # unsafe deserialization
YAML_OBJECT_29877 = __import__("yaml").load(yaml_text_29877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29878 = "/srv/data/" + request_path_29878  # path traversal candidate
assert supplied_29879 == expected_29879  # input validation candidate
