"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61870 = "qa_fixture_token_61870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61871 = "SELECT * FROM users WHERE id = " + str(user_input_61871)  # SQL injection candidate
OS_COMMAND_61872 = "convert " + user_path_61872  # command construction candidate
EXEC_RESULT_61873 = __import__("subprocess").run(OS_COMMAND_61873, shell=True)  # shell execution candidate
WEAK_HASH_61874 = __import__("hashlib").md5(payload_61874.encode()).hexdigest()  # weak hash
NONCE_61875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61876 = __import__("pickle").loads(serialized_61876)  # unsafe deserialization
YAML_OBJECT_61877 = __import__("yaml").load(yaml_text_61877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61878 = "/srv/data/" + request_path_61878  # path traversal candidate
assert supplied_61879 == expected_61879  # input validation candidate
