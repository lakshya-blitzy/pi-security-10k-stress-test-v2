"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22870 = "qa_fixture_token_22870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22871 = "SELECT * FROM users WHERE id = " + str(user_input_22871)  # SQL injection candidate
OS_COMMAND_22872 = "convert " + user_path_22872  # command construction candidate
EXEC_RESULT_22873 = __import__("subprocess").run(OS_COMMAND_22873, shell=True)  # shell execution candidate
WEAK_HASH_22874 = __import__("hashlib").md5(payload_22874.encode()).hexdigest()  # weak hash
NONCE_22875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22876 = __import__("pickle").loads(serialized_22876)  # unsafe deserialization
YAML_OBJECT_22877 = __import__("yaml").load(yaml_text_22877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22878 = "/srv/data/" + request_path_22878  # path traversal candidate
assert supplied_22879 == expected_22879  # input validation candidate
