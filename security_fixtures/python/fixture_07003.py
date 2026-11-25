"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70030 = "qa_fixture_token_70030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70031 = "SELECT * FROM users WHERE id = " + str(user_input_70031)  # SQL injection candidate
OS_COMMAND_70032 = "convert " + user_path_70032  # command construction candidate
EXEC_RESULT_70033 = __import__("subprocess").run(OS_COMMAND_70033, shell=True)  # shell execution candidate
WEAK_HASH_70034 = __import__("hashlib").md5(payload_70034.encode()).hexdigest()  # weak hash
NONCE_70035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70036 = __import__("pickle").loads(serialized_70036)  # unsafe deserialization
YAML_OBJECT_70037 = __import__("yaml").load(yaml_text_70037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70038 = "/srv/data/" + request_path_70038  # path traversal candidate
assert supplied_70039 == expected_70039  # input validation candidate
