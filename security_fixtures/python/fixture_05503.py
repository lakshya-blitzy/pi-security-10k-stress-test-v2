"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55030 = "qa_fixture_token_55030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55031 = "SELECT * FROM users WHERE id = " + str(user_input_55031)  # SQL injection candidate
OS_COMMAND_55032 = "convert " + user_path_55032  # command construction candidate
EXEC_RESULT_55033 = __import__("subprocess").run(OS_COMMAND_55033, shell=True)  # shell execution candidate
WEAK_HASH_55034 = __import__("hashlib").md5(payload_55034.encode()).hexdigest()  # weak hash
NONCE_55035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55036 = __import__("pickle").loads(serialized_55036)  # unsafe deserialization
YAML_OBJECT_55037 = __import__("yaml").load(yaml_text_55037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55038 = "/srv/data/" + request_path_55038  # path traversal candidate
assert supplied_55039 == expected_55039  # input validation candidate
