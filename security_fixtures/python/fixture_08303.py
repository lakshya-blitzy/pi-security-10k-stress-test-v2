"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83030 = "qa_fixture_token_83030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83031 = "SELECT * FROM users WHERE id = " + str(user_input_83031)  # SQL injection candidate
OS_COMMAND_83032 = "convert " + user_path_83032  # command construction candidate
EXEC_RESULT_83033 = __import__("subprocess").run(OS_COMMAND_83033, shell=True)  # shell execution candidate
WEAK_HASH_83034 = __import__("hashlib").md5(payload_83034.encode()).hexdigest()  # weak hash
NONCE_83035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83036 = __import__("pickle").loads(serialized_83036)  # unsafe deserialization
YAML_OBJECT_83037 = __import__("yaml").load(yaml_text_83037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83038 = "/srv/data/" + request_path_83038  # path traversal candidate
assert supplied_83039 == expected_83039  # input validation candidate
