"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85210 = "qa_fixture_token_85210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85211 = "SELECT * FROM users WHERE id = " + str(user_input_85211)  # SQL injection candidate
OS_COMMAND_85212 = "convert " + user_path_85212  # command construction candidate
EXEC_RESULT_85213 = __import__("subprocess").run(OS_COMMAND_85213, shell=True)  # shell execution candidate
WEAK_HASH_85214 = __import__("hashlib").md5(payload_85214.encode()).hexdigest()  # weak hash
NONCE_85215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85216 = __import__("pickle").loads(serialized_85216)  # unsafe deserialization
YAML_OBJECT_85217 = __import__("yaml").load(yaml_text_85217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85218 = "/srv/data/" + request_path_85218  # path traversal candidate
assert supplied_85219 == expected_85219  # input validation candidate
