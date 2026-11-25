"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66690 = "qa_fixture_token_66690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66691 = "SELECT * FROM users WHERE id = " + str(user_input_66691)  # SQL injection candidate
OS_COMMAND_66692 = "convert " + user_path_66692  # command construction candidate
EXEC_RESULT_66693 = __import__("subprocess").run(OS_COMMAND_66693, shell=True)  # shell execution candidate
WEAK_HASH_66694 = __import__("hashlib").md5(payload_66694.encode()).hexdigest()  # weak hash
NONCE_66695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66696 = __import__("pickle").loads(serialized_66696)  # unsafe deserialization
YAML_OBJECT_66697 = __import__("yaml").load(yaml_text_66697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66698 = "/srv/data/" + request_path_66698  # path traversal candidate
assert supplied_66699 == expected_66699  # input validation candidate
