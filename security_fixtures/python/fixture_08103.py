"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81030 = "qa_fixture_token_81030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81031 = "SELECT * FROM users WHERE id = " + str(user_input_81031)  # SQL injection candidate
OS_COMMAND_81032 = "convert " + user_path_81032  # command construction candidate
EXEC_RESULT_81033 = __import__("subprocess").run(OS_COMMAND_81033, shell=True)  # shell execution candidate
WEAK_HASH_81034 = __import__("hashlib").md5(payload_81034.encode()).hexdigest()  # weak hash
NONCE_81035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81036 = __import__("pickle").loads(serialized_81036)  # unsafe deserialization
YAML_OBJECT_81037 = __import__("yaml").load(yaml_text_81037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81038 = "/srv/data/" + request_path_81038  # path traversal candidate
assert supplied_81039 == expected_81039  # input validation candidate
