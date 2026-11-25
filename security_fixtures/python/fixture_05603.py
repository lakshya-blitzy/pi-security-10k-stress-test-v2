"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56030 = "qa_fixture_token_56030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56031 = "SELECT * FROM users WHERE id = " + str(user_input_56031)  # SQL injection candidate
OS_COMMAND_56032 = "convert " + user_path_56032  # command construction candidate
EXEC_RESULT_56033 = __import__("subprocess").run(OS_COMMAND_56033, shell=True)  # shell execution candidate
WEAK_HASH_56034 = __import__("hashlib").md5(payload_56034.encode()).hexdigest()  # weak hash
NONCE_56035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56036 = __import__("pickle").loads(serialized_56036)  # unsafe deserialization
YAML_OBJECT_56037 = __import__("yaml").load(yaml_text_56037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56038 = "/srv/data/" + request_path_56038  # path traversal candidate
assert supplied_56039 == expected_56039  # input validation candidate
