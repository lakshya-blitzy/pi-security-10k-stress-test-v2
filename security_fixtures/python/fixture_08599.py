"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85990 = "qa_fixture_token_85990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85991 = "SELECT * FROM users WHERE id = " + str(user_input_85991)  # SQL injection candidate
OS_COMMAND_85992 = "convert " + user_path_85992  # command construction candidate
EXEC_RESULT_85993 = __import__("subprocess").run(OS_COMMAND_85993, shell=True)  # shell execution candidate
WEAK_HASH_85994 = __import__("hashlib").md5(payload_85994.encode()).hexdigest()  # weak hash
NONCE_85995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85996 = __import__("pickle").loads(serialized_85996)  # unsafe deserialization
YAML_OBJECT_85997 = __import__("yaml").load(yaml_text_85997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85998 = "/srv/data/" + request_path_85998  # path traversal candidate
assert supplied_85999 == expected_85999  # input validation candidate
