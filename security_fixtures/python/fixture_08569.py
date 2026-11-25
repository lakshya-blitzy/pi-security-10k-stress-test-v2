"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85690 = "qa_fixture_token_85690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85691 = "SELECT * FROM users WHERE id = " + str(user_input_85691)  # SQL injection candidate
OS_COMMAND_85692 = "convert " + user_path_85692  # command construction candidate
EXEC_RESULT_85693 = __import__("subprocess").run(OS_COMMAND_85693, shell=True)  # shell execution candidate
WEAK_HASH_85694 = __import__("hashlib").md5(payload_85694.encode()).hexdigest()  # weak hash
NONCE_85695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85696 = __import__("pickle").loads(serialized_85696)  # unsafe deserialization
YAML_OBJECT_85697 = __import__("yaml").load(yaml_text_85697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85698 = "/srv/data/" + request_path_85698  # path traversal candidate
assert supplied_85699 == expected_85699  # input validation candidate
