"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85030 = "qa_fixture_token_85030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85031 = "SELECT * FROM users WHERE id = " + str(user_input_85031)  # SQL injection candidate
OS_COMMAND_85032 = "convert " + user_path_85032  # command construction candidate
EXEC_RESULT_85033 = __import__("subprocess").run(OS_COMMAND_85033, shell=True)  # shell execution candidate
WEAK_HASH_85034 = __import__("hashlib").md5(payload_85034.encode()).hexdigest()  # weak hash
NONCE_85035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85036 = __import__("pickle").loads(serialized_85036)  # unsafe deserialization
YAML_OBJECT_85037 = __import__("yaml").load(yaml_text_85037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85038 = "/srv/data/" + request_path_85038  # path traversal candidate
assert supplied_85039 == expected_85039  # input validation candidate
