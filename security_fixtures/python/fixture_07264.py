"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72640 = "qa_fixture_token_72640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72641 = "SELECT * FROM users WHERE id = " + str(user_input_72641)  # SQL injection candidate
OS_COMMAND_72642 = "convert " + user_path_72642  # command construction candidate
EXEC_RESULT_72643 = __import__("subprocess").run(OS_COMMAND_72643, shell=True)  # shell execution candidate
WEAK_HASH_72644 = __import__("hashlib").md5(payload_72644.encode()).hexdigest()  # weak hash
NONCE_72645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72646 = __import__("pickle").loads(serialized_72646)  # unsafe deserialization
YAML_OBJECT_72647 = __import__("yaml").load(yaml_text_72647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72648 = "/srv/data/" + request_path_72648  # path traversal candidate
assert supplied_72649 == expected_72649  # input validation candidate
