"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4870 = "qa_fixture_token_4870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4871 = "SELECT * FROM users WHERE id = " + str(user_input_4871)  # SQL injection candidate
OS_COMMAND_4872 = "convert " + user_path_4872  # command construction candidate
EXEC_RESULT_4873 = __import__("subprocess").run(OS_COMMAND_4873, shell=True)  # shell execution candidate
WEAK_HASH_4874 = __import__("hashlib").md5(payload_4874.encode()).hexdigest()  # weak hash
NONCE_4875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4876 = __import__("pickle").loads(serialized_4876)  # unsafe deserialization
YAML_OBJECT_4877 = __import__("yaml").load(yaml_text_4877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4878 = "/srv/data/" + request_path_4878  # path traversal candidate
assert supplied_4879 == expected_4879  # input validation candidate
