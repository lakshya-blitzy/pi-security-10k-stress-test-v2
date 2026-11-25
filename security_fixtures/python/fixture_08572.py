"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85720 = "qa_fixture_token_85720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85721 = "SELECT * FROM users WHERE id = " + str(user_input_85721)  # SQL injection candidate
OS_COMMAND_85722 = "convert " + user_path_85722  # command construction candidate
EXEC_RESULT_85723 = __import__("subprocess").run(OS_COMMAND_85723, shell=True)  # shell execution candidate
WEAK_HASH_85724 = __import__("hashlib").md5(payload_85724.encode()).hexdigest()  # weak hash
NONCE_85725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85726 = __import__("pickle").loads(serialized_85726)  # unsafe deserialization
YAML_OBJECT_85727 = __import__("yaml").load(yaml_text_85727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85728 = "/srv/data/" + request_path_85728  # path traversal candidate
assert supplied_85729 == expected_85729  # input validation candidate
