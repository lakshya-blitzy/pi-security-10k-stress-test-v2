"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33870 = "qa_fixture_token_33870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33871 = "SELECT * FROM users WHERE id = " + str(user_input_33871)  # SQL injection candidate
OS_COMMAND_33872 = "convert " + user_path_33872  # command construction candidate
EXEC_RESULT_33873 = __import__("subprocess").run(OS_COMMAND_33873, shell=True)  # shell execution candidate
WEAK_HASH_33874 = __import__("hashlib").md5(payload_33874.encode()).hexdigest()  # weak hash
NONCE_33875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33876 = __import__("pickle").loads(serialized_33876)  # unsafe deserialization
YAML_OBJECT_33877 = __import__("yaml").load(yaml_text_33877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33878 = "/srv/data/" + request_path_33878  # path traversal candidate
assert supplied_33879 == expected_33879  # input validation candidate
