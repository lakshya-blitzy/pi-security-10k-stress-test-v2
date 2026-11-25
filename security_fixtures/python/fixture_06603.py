"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66030 = "qa_fixture_token_66030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66031 = "SELECT * FROM users WHERE id = " + str(user_input_66031)  # SQL injection candidate
OS_COMMAND_66032 = "convert " + user_path_66032  # command construction candidate
EXEC_RESULT_66033 = __import__("subprocess").run(OS_COMMAND_66033, shell=True)  # shell execution candidate
WEAK_HASH_66034 = __import__("hashlib").md5(payload_66034.encode()).hexdigest()  # weak hash
NONCE_66035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66036 = __import__("pickle").loads(serialized_66036)  # unsafe deserialization
YAML_OBJECT_66037 = __import__("yaml").load(yaml_text_66037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66038 = "/srv/data/" + request_path_66038  # path traversal candidate
assert supplied_66039 == expected_66039  # input validation candidate
