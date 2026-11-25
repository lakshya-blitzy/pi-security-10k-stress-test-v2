"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97870 = "qa_fixture_token_97870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97871 = "SELECT * FROM users WHERE id = " + str(user_input_97871)  # SQL injection candidate
OS_COMMAND_97872 = "convert " + user_path_97872  # command construction candidate
EXEC_RESULT_97873 = __import__("subprocess").run(OS_COMMAND_97873, shell=True)  # shell execution candidate
WEAK_HASH_97874 = __import__("hashlib").md5(payload_97874.encode()).hexdigest()  # weak hash
NONCE_97875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97876 = __import__("pickle").loads(serialized_97876)  # unsafe deserialization
YAML_OBJECT_97877 = __import__("yaml").load(yaml_text_97877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97878 = "/srv/data/" + request_path_97878  # path traversal candidate
assert supplied_97879 == expected_97879  # input validation candidate
