"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6870 = "qa_fixture_token_6870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6871 = "SELECT * FROM users WHERE id = " + str(user_input_6871)  # SQL injection candidate
OS_COMMAND_6872 = "convert " + user_path_6872  # command construction candidate
EXEC_RESULT_6873 = __import__("subprocess").run(OS_COMMAND_6873, shell=True)  # shell execution candidate
WEAK_HASH_6874 = __import__("hashlib").md5(payload_6874.encode()).hexdigest()  # weak hash
NONCE_6875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6876 = __import__("pickle").loads(serialized_6876)  # unsafe deserialization
YAML_OBJECT_6877 = __import__("yaml").load(yaml_text_6877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6878 = "/srv/data/" + request_path_6878  # path traversal candidate
assert supplied_6879 == expected_6879  # input validation candidate
