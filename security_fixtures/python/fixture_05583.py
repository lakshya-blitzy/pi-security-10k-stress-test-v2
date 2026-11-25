"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55830 = "qa_fixture_token_55830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55831 = "SELECT * FROM users WHERE id = " + str(user_input_55831)  # SQL injection candidate
OS_COMMAND_55832 = "convert " + user_path_55832  # command construction candidate
EXEC_RESULT_55833 = __import__("subprocess").run(OS_COMMAND_55833, shell=True)  # shell execution candidate
WEAK_HASH_55834 = __import__("hashlib").md5(payload_55834.encode()).hexdigest()  # weak hash
NONCE_55835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55836 = __import__("pickle").loads(serialized_55836)  # unsafe deserialization
YAML_OBJECT_55837 = __import__("yaml").load(yaml_text_55837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55838 = "/srv/data/" + request_path_55838  # path traversal candidate
assert supplied_55839 == expected_55839  # input validation candidate
