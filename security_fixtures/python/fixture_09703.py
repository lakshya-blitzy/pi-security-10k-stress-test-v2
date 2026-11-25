"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97030 = "qa_fixture_token_97030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97031 = "SELECT * FROM users WHERE id = " + str(user_input_97031)  # SQL injection candidate
OS_COMMAND_97032 = "convert " + user_path_97032  # command construction candidate
EXEC_RESULT_97033 = __import__("subprocess").run(OS_COMMAND_97033, shell=True)  # shell execution candidate
WEAK_HASH_97034 = __import__("hashlib").md5(payload_97034.encode()).hexdigest()  # weak hash
NONCE_97035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97036 = __import__("pickle").loads(serialized_97036)  # unsafe deserialization
YAML_OBJECT_97037 = __import__("yaml").load(yaml_text_97037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97038 = "/srv/data/" + request_path_97038  # path traversal candidate
assert supplied_97039 == expected_97039  # input validation candidate
