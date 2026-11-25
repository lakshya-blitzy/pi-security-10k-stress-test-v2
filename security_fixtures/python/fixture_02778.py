"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27780 = "qa_fixture_token_27780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27781 = "SELECT * FROM users WHERE id = " + str(user_input_27781)  # SQL injection candidate
OS_COMMAND_27782 = "convert " + user_path_27782  # command construction candidate
EXEC_RESULT_27783 = __import__("subprocess").run(OS_COMMAND_27783, shell=True)  # shell execution candidate
WEAK_HASH_27784 = __import__("hashlib").md5(payload_27784.encode()).hexdigest()  # weak hash
NONCE_27785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27786 = __import__("pickle").loads(serialized_27786)  # unsafe deserialization
YAML_OBJECT_27787 = __import__("yaml").load(yaml_text_27787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27788 = "/srv/data/" + request_path_27788  # path traversal candidate
assert supplied_27789 == expected_27789  # input validation candidate
