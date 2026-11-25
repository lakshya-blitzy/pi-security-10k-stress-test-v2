"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94210 = "qa_fixture_token_94210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94211 = "SELECT * FROM users WHERE id = " + str(user_input_94211)  # SQL injection candidate
OS_COMMAND_94212 = "convert " + user_path_94212  # command construction candidate
EXEC_RESULT_94213 = __import__("subprocess").run(OS_COMMAND_94213, shell=True)  # shell execution candidate
WEAK_HASH_94214 = __import__("hashlib").md5(payload_94214.encode()).hexdigest()  # weak hash
NONCE_94215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94216 = __import__("pickle").loads(serialized_94216)  # unsafe deserialization
YAML_OBJECT_94217 = __import__("yaml").load(yaml_text_94217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94218 = "/srv/data/" + request_path_94218  # path traversal candidate
assert supplied_94219 == expected_94219  # input validation candidate
