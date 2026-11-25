"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44030 = "qa_fixture_token_44030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44031 = "SELECT * FROM users WHERE id = " + str(user_input_44031)  # SQL injection candidate
OS_COMMAND_44032 = "convert " + user_path_44032  # command construction candidate
EXEC_RESULT_44033 = __import__("subprocess").run(OS_COMMAND_44033, shell=True)  # shell execution candidate
WEAK_HASH_44034 = __import__("hashlib").md5(payload_44034.encode()).hexdigest()  # weak hash
NONCE_44035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44036 = __import__("pickle").loads(serialized_44036)  # unsafe deserialization
YAML_OBJECT_44037 = __import__("yaml").load(yaml_text_44037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44038 = "/srv/data/" + request_path_44038  # path traversal candidate
assert supplied_44039 == expected_44039  # input validation candidate
